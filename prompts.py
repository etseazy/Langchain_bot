from langchain.prompts import PromptTemplate

# This prompt will help the LLM extract key points from the counseling transcript
extraction_prompt = PromptTemplate(
    input_variables=["transcript"],
    template="""
You are an AI assistant trained to analyze transcripts of career counseling sessions between a student and a counselor.

Read the following transcript carefully and extract two sets of information:
1. **Career Goals**: What are the student's stated or implied career interests, aspirations, or long-term goals?
2. **Action Items**: What concrete steps, suggestions, or strategies did the counselor recommend to help the student progress?

--- Transcript Start ---
{transcript}
--- Transcript End ---

Return your response under the following headings:

Career Goals:
- (bullet points)

Action Items:
- (bullet points)

Be concise and accurate. Do not invent or assume information not present in the transcript.
"""
)

# This prompt will turn the extracted info into an email
email_prompt = PromptTemplate(
    input_variables=["student_name", "takeaways"],
    template="""
You are a warm, supportive career counseling assistant.

Using the extracted takeaways from a recent counseling session, write a follow-up email to the student {student_name}.

Your email should:
- Greet the student by name
- Reaffirm their career goals
- Clearly list the suggested action items
- End with an encouraging and positive message, reinforcing your availability for further help

Use a friendly and motivational tone — the goal is to make the student feel supported and confident.

Here are the takeaways:
{takeaways}

--- Begin Email Below ---
"""
)
