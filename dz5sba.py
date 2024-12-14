from datetime import datetime

moscow_times = 'The Moscow Times - Wednesday, October 2, 2002'
guardian = 'The Guardian - Friday, 11.10.13'
d_news = 'Daily News - Thursday, 18 August 1977'

datetime.strptime(moscow_times[30:45], '%B %d, %Y')
datetime.strptime(guardian[23:31], '%d.%m.%y')
datetime.strptime(d_news[23:37], '%d %B %Y')