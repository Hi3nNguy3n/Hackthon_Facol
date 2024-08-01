from model import get_response
from translate import vi_en, en_vi

user_input = "Tôi cảm thấy khớp gối của tôi bị đau nhứt"

response = get_response(vi_en(user_input))
print(en_vi(response))