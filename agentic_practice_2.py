# Practice Exercise Solutions for Agentic Patterns

from typing import TypedDict, Literal, Annotated
from pydantic import BaseModel, Field
import operator

# ============================================================================
# EXERCISE 1: Adaptive Reflection with Quality Metrics
# ============================================================================

class QualityScore(BaseModel):
    """Quality scoring model."""
    clarity: int = Field(description="Clarity score (1-5)", ge=1, le=5)
    completeness: int = Field(description="Completeness score (1-5)", ge=1, le=5)
    accuracy: int = Field(description="Accuracy score (1-5)", ge=1, le=5)
    reasoning: str = Field(description="Explanation of scores")

class MetricReflectionState(TypedDict):
    """State for metric-based reflection."""
    task: str
    draft: str
    scores: list[QualityScore]
    critique: str
    iterations: int
    final_output: str

MAX_METRIC_ITERATIONS = 3
QUALITY_THRESHOLD = 4

# Nodes
def metric_generator(state: MetricReflectionState) -> dict:
    """Generate or refine based on critique."""
    if state["iterations"] == 0:
        prompt = f"Create a response for: {state['task']}"
        print("\n✍️ Generating initial draft...")
    else:
        prompt = f"""Improve this draft:

Task: {state['task']}
Draft: {state['draft']}
Critique: {state['critique']}

Create improved version."""
        print(f"\n✍️ Refining (iteration {state['iterations']})...")
    
    response = llm.invoke([HumanMessage(content=prompt)])
    print("✓ Draft created\n")
    return {"draft": response.content}

def metric_critic(state: MetricReflectionState) -> dict:
    """Score draft on quality metrics."""
    llm_with_structure = llm.with_structured_output(QualityScore)
    
    prompt = f"""Evaluate this response:

Task: {state['task']}
Response: {state['draft']}

Score on:
- Clarity (1-5): How clear and understandable?
- Completeness (1-5): How complete is the answer?
- Accuracy (1-5): How accurate is the information?

Provide scores and reasoning."""
    
    print("🔍 Scoring draft...")
    score = llm_with_structure.invoke([HumanMessage(content=prompt)])
    
    print(f"Scores - Clarity: {score.clarity}, Completeness: {score.completeness}, Accuracy: {score.accuracy}")
    print(f"Reasoning: {score.reasoning[:80]}...\n")
    
    # Build critique from low scores
    low_scores = []
    if score.clarity < QUALITY_THRESHOLD:
        low_scores.append(f"Clarity needs improvement (score: {score.clarity})")
    if score.completeness < QUALITY_THRESHOLD:
        low_scores.append(f"Completeness needs work (score: {score.completeness})")
    if score.accuracy < QUALITY_THRESHOLD:
        low_scores.append(f"Accuracy could be better (score: {score.accuracy})")
    
    critique = "; ".join(low_scores) if low_scores else "APPROVED"
    
    return {
        "scores": [score],
        "critique": critique,
        "iterations": state["iterations"] + 1
    }

def metric_finalizer(state: MetricReflectionState) -> dict:
    """Finalize with score summary."""
    print("\n✅ Reflection complete!\n")
    
    # Show score progression
    if state["scores"]:
        print("📊 Score Progression:")
        for i, score in enumerate(state["scores"], 1):
            print(f"  Iteration {i}: Clarity={score.clarity}, Completeness={score.completeness}, Accuracy={score.accuracy}")
        print()
    
    return {"final_output": state["draft"]}

def should_metric_reflect(state: MetricReflectionState) -> Literal["generator", "finalizer"]:
    """Check if all scores meet threshold."""
    if not state.get("scores"):
        return "generator"
    
    latest_score = state["scores"][-1]
    all_good = (latest_score.clarity >= QUALITY_THRESHOLD and 
                latest_score.completeness >= QUALITY_THRESHOLD and 
                latest_score.accuracy >= QUALITY_THRESHOLD)
    
    if all_good or state["iterations"] >= MAX_METRIC_ITERATIONS:
        return "finalizer"
    
    return "generator"

# Build graph
metric_reflection_builder = StateGraph(MetricReflectionState)
metric_reflection_builder.add_node("generator", metric_generator)
metric_reflection_builder.add_node("critic", metric_critic)
metric_reflection_builder.add_node("finalizer", metric_finalizer)

metric_reflection_builder.add_edge(START, "generator")
metric_reflection_builder.add_edge("generator", "critic")
metric_reflection_builder.add_conditional_edges(
    "critic",
    should_metric_reflect,
    {"generator": "generator", "finalizer": "finalizer"}
)
metric_reflection_builder.add_edge("finalizer", END)

metric_reflection_agent = metric_reflection_builder.compile()


# ============================================================================
# EXERCISE 2: Plan-Execute + Reflection Hybrid
# ============================================================================

class HybridState(TypedDict):
    """Combined Plan-Execute and Reflection state."""
    # Plan-Execute fields
    input: str
    plan: list[str]
    current_step: int
    results: Annotated[list[str], operator.add]
    
    # Reflection fields
    draft: str
    critique: str
    reflection_iterations: int
    
    # Final
    final_output: str

MAX_HYBRID_REFLECTIONS = 2

# Nodes
def hybrid_planner(state: HybridState) -> dict:
    """Create execution plan."""
    prompt = f"""Create a 3-4 step plan for: {state['input']}

Return numbered list of concrete steps."""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    lines = response.content.split('\n')
    steps = [line.strip() for line in lines if line.strip() and any(c.isdigit() for c in line[:3])]
    
    print(f"\n📋 PLAN:")
    for step in steps:
        print(f"  {step}")
    print()
    
    return {"plan": steps, "current_step": 0, "results": [], "reflection_iterations": 0}

def hybrid_executor(state: HybridState) -> dict:
    """Execute current step."""
    if state["current_step"] >= len(state["plan"]):
        return {}
    
    current_step = state["plan"][state["current_step"]]
    print(f"⚙️ Executing: {current_step}")
    
    prompt = f"Previous: {state.get('results', [])}\n\nExecute: {current_step}"
    response = llm.invoke([HumanMessage(content=prompt)])
    
    result = f"Step {state['current_step'] + 1}: {response.content}"
    print(f"✓ Done\n")
    
    return {
        "results": [result],
        "current_step": state["current_step"] + 1
    }

def hybrid_generator(state: HybridState) -> dict:
    """Synthesize results into draft."""
    if state["reflection_iterations"] == 0:
        prompt = f"""Create final answer from these results:

Task: {state['input']}
Results: {state['results']}

Provide clear, concise answer."""
        print("\n✍️ Generating draft from results...")
    else:
        prompt = f"""Improve based on critique:

Task: {state['input']}
Draft: {state['draft']}
Critique: {state['critique']}

Create improved version."""
        print(f"\n✍️ Refining draft (iteration {state['reflection_iterations']})...")
    
    response = llm.invoke([HumanMessage(content=prompt)])
    print("✓ Draft ready\n")
    
    return {"draft": response.content}

def hybrid_critic(state: HybridState) -> dict:
    """Critique the complete output."""
    prompt = f"""Evaluate this response:

Task: {state['input']}
Response: {state['draft']}

If excellent, say "APPROVED: reason".
Otherwise, provide specific improvements."""
    
    print("🔍 Critiquing output...")
    response = llm.invoke([HumanMessage(content=prompt)])
    critique = response.content
    
    print(f"Critique: {critique[:80]}...\n")
    
    return {
        "critique": critique,
        "reflection_iterations": state["reflection_iterations"] + 1
    }

def hybrid_finalizer(state: HybridState) -> dict:
    """Set final output."""
    print("\n✅ Hybrid agent complete!\n")
    return {"final_output": state["draft"]}

# Routing
def should_execute_more(state: HybridState) -> Literal["executor", "generator"]:
    """Continue execution or move to generation?"""
    if state["current_step"] < len(state["plan"]):
        return "executor"
    return "generator"

def should_reflect_hybrid(state: HybridState) -> Literal["generator", "finalizer"]:
    """Reflect again or finalize?"""
    if "APPROVED" in state.get("critique", "").upper():
        return "finalizer"
    
    if state["reflection_iterations"] >= MAX_HYBRID_REFLECTIONS:
        print(f"⚠️ Max reflections ({MAX_HYBRID_REFLECTIONS}) reached\n")
        return "finalizer"
    
    return "generator"

# Build graph
hybrid_builder = StateGraph(HybridState)

hybrid_builder.add_node("planner", hybrid_planner)
hybrid_builder.add_node("executor", hybrid_executor)
hybrid_builder.add_node("generator", hybrid_generator)
hybrid_builder.add_node("critic", hybrid_critic)
hybrid_builder.add_node("finalizer", hybrid_finalizer)

hybrid_builder.add_edge(START, "planner")
hybrid_builder.add_edge("planner", "executor")
hybrid_builder.add_conditional_edges(
    "executor",
    should_execute_more,
    {"executor": "executor", "generator": "generator"}
)
hybrid_builder.add_edge("generator", "critic")
hybrid_builder.add_conditional_edges(
    "critic",
    should_reflect_hybrid,
    {"generator": "generator", "finalizer": "finalizer"}
)
hybrid_builder.add_edge("finalizer", END)

hybrid_agent = hybrid_builder.compile()


# ============================================================================
# TEST EXERCISES
# ============================================================================

print("="*80)
print("EXERCISE 1: Metric-Based Reflection")
print("="*80)

result1 = metric_reflection_agent.invoke({
    "task": "Explain quantum computing in simple terms",
    "draft": "",
    "scores": [],
    "critique": "",
    "iterations": 0
})

print(f"\n{'='*70}")
print("📊 FINAL OUTPUT:")
print(f"{'='*70}")
print(result1["final_output"])
print(f"\nTotal iterations: {result1['iterations']}")
print(f"{'='*70}\n")


print("\n" + "="*80)
print("EXERCISE 2: Plan-Execute + Reflection Hybrid")
print("="*80)

result2 = hybrid_agent.invoke({
    "input": "Research Python benefits and create beginner-friendly summary"
})

print(f"\n{'='*70}")
print("📊 FINAL OUTPUT:")
print(f"{'='*70}")
print(result2["final_output"])
print(f"{'='*70}\n")
