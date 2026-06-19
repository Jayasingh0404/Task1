from fastapi import FastAPI, HTTPException, status
from app.schemas import EvaluationRequest, EvaluationResponse
from app.evaluator import evaluate_answer
import logging

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Answer Evaluation Engine API",
    description="Automated system to evaluate technical candidate answers using a hybrid rule-based and LLM approach.",
    version="1.0.0"
)

@app.get("/health", status_code=status.HTTP_200_OK, tags=["Health"])
async def health_check():
    """Simple health check endpoint to verify the service is running."""
    return {"status": "healthy"}

@app.post("/evaluate", response_model=EvaluationResponse, status_code=status.HTTP_200_OK, tags=["Evaluation"])
async def evaluate(payload: EvaluationRequest):
    """
    Evaluates candidate answers to technical questions.
    
    Checks for relevance, completeness, and correctness using a rule-based pre-filter
    and falls back/augments via OpenAI/Gemini LLM API calls.
    """
    try:
        result = evaluate_answer(
            question=payload.question,
            answer=payload.answer,
            domain=payload.domain
        )
        return EvaluationResponse(**result)
    except Exception as e:
        logger.error(f"Internal server error during evaluation: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Evaluation failed: {str(e)}"
        )
