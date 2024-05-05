from starlette.exceptions import HTTPException

from utils.helper import get_suggestions
from utils.models import Conversation
from utils.enums import HttpStatusCode
from utils.prompts import SUGGESTION_PROMPT


def suggestions(conversationRequest: Conversation):
    try:
        conversation_history = conversationRequest.conversation_history
        calling_purpose = conversationRequest.calling_purpose
        response = get_suggestions(conversation_history, calling_purpose)
        return response
    except Exception as exception:
        raise HTTPException(
            status_code=HttpStatusCode.INTERNAL_SERVER_ERROR.value,
            detail=f"An error occured while generating suggestions!\n{str(exception.__class__)}",
        )
