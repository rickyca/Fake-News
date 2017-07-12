import pandas as pd

df = pd.DataFrame(columns=[u'baseline', u'score', u'steps', u'details', u'predicted_fake__fake',
                    u'predicted_real__fake', u'predicted_fake__real',
                    u'predicted_real__real'])
df.to_csv('log.csv', index=False)
