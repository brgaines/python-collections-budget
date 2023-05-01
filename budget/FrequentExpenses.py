# Module 1

# %%
from . import Expense
# import Expense
import collections
import matplotlib.pyplot as plt

# %%
expenses = Expense.Expenses()

# %%
# Import data
expenses.read_expenses('data/spending_data.csv')
# %%
spending_categories = []
# spending_categories = list()
# Tests failed with list() for soe reason

# %%
# Extract expense categories
for expense in expenses.list:
    spending_categories.append(expense.category)

# %% Count the categories
spending_counter = collections.Counter(spending_categories)
print(spending_counter)

# %%
top5 = spending_counter.most_common(5)
print(top5)
# %%
categories, count = zip(*top5)
print(categories, count)

# %%
fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()
# These commands all had to be in the same cell for some reason.
