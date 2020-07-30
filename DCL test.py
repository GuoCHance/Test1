from lifelines.datasets import load_waltons
from lifelines import KaplanMeierFitter
from lifelines.utils import median_survival_times

df = load_waltons()
print(df.head(),'\n')
print(df['T'].min(), df['T'].max(),'\n')
print(df['E'].value_counts(),'\n')
print(df['group'].value_counts(),'\n')

kmf = KaplanMeierFitter()
kmf.fit(df['T'], event_observed=df['E'])

kmf.plot_survival_function()

median_ = kmf.median_survival_time_
median_confidence_interval_ = median_survival_times(kmf.confidence_interval_)
print(median_confidence_interval_)
