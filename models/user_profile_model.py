from pydantic import BaseModel

class UserProfileModel(BaseModel):
    uid: str
    score_btech: float
    gap_years: float
    project_experience: int
    project_count: int
    self_assesment_english_spoken: int
    self_assesment_email_writing: int
    self_assesment_aptitude_logic: int
    self_assesment_aptitude_quantitative: int
    self_assesment_time_management: int
    self_assesment_self_introduction: int
    self_assesment_public_speaking: int
    self_assesment_group_discussion: int
    self_assesment_presentation_skills: int
    self_assesment_industry_assesment: int
    self_assesment_timely_completion: int
    self_assesment_work_under_pressure: int
    self_assesment_learning_new_skills: int
    self_assesment_preparation_for_working_long_hours: int
    priority_for_job_in_career: int
    priority_for_monetory_benifits: int
    priority_for_convinience_at_work: int
    priority_for_job_role_in_career: int

class PredictionResponse(BaseModel):
    uid: str
    prediction: float