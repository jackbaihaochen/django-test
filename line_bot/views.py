from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse
from django.contrib import messages
from line_bot.line_bot import LineAuth, LineBot


USER_ID = 'bai.jack@jackbai'
DOMAIN_ID = '500023959'
TEST_BOT_ID = '1416858'
TEST_BOT = LineBot(LineAuth().get_access_token(), TEST_BOT_ID)


# The following methods are for render
# This is the home page for line_bot app.
def index(request, *args, **kwargs):
    # domain_member_list = (test_bot.get_domain_member_list(500023959))['member_list']
    result = request.GET.dict().get('result')
    return render(request, 'index.html', {'result': result})


# The following methods are of special functions
def send_message_to_one(request):
    try:
        user_id = request.POST.get('user_id')
        message = request.POST.get('msg')
    except MultiValueDictKeyError:
        messages.warning(request, 'Please enter User Id and Message correctly.')
        return HttpResponseRedirect(reverse('line_bot:home'))
    send_message_response = TEST_BOT.send_message_to_one(user_id, message)
    messages.success(request, 'Succeeded!') if send_message_response else messages.error(request, 'Failed!')
    return HttpResponseRedirect(reverse('line_bot:home'))


