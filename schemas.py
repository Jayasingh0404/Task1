from pydantic import BaseModel, Field
from typing import Optional

class EvaluationRequest(BaseModel):
    question: str = Field(..., description="The technical question asked to the candidate.")
    answer: str = Field(..., description="The candidate's response to be evaluated.")
    domain: Optional[str] = Field(
        None, 
        description="The technical domain of the question (e.g., 'dsa', 'dbms', 'os'). If omitted, it will be auto-detected."
    )

class EvaluationResponse(BaseModel):
    score: float = Field(..., ge=0.0, le=10.0, description="The evaluation score out of 10.")
    feedback: str = Field(..., description="Constructive feedback explaining the score and any missing or incorrect points.")
    confidence: float = Field(..., ge=0.0, le=1.0, description="The confidence level of the evaluation score.")
