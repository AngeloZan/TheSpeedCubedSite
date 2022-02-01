from .forms import FeedbackForm

def feedback_form(request):
    if request.method == 'GET':
        feedback_form = FeedbackForm()
        return {'feedback_form': feedback_form}
    return {}
