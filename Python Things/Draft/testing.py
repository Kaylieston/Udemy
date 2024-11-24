import pandas as pd
import random

# Define the fields
fields = ["Content name", "Content type", "Communities name", "Username"]

# Define possible values for content types
content_types = ["wiki", "post with documents", "forum", "poll title"]

# Generate 50 rows with at least one common word
common_words = ["Python", "Data", "Machine", "Learning", "AI", "Cloud", "Security", "Web", "Development", "Finance"]
data = []

for _ in range(50):
    word = random.choice(common_words)
    content_name = f"{word} {random.choice(['Basics', 'Advanced', 'Techniques', 'Guide', 'Tutorial'])}"
    community_name = f"{word} {random.choice(['Community', 'Group', 'Enthusiasts', 'Experts'])}"
    username = f"{word}{random.randint(1, 1000)}"
    content_type = random.choice(content_types)
    data.append([content_name, content_type, community_name, username])

# Generate 200 random rows
for _ in range(200):
    content_name = f"{random.choice(['JavaScript', 'Java', 'C++', 'Ruby', 'Go', 'Swift', 'Kotlin', 'PHP', 'HTML', 'CSS'])} {random.choice(['Basics', 'Advanced', 'Techniques', 'Guide', 'Tutorial'])}"
    community_name = f"{random.choice(['Programming', 'Development', 'Coding', 'Software', 'Tech', 'IT', 'Engineering', 'Science', 'Math', 'Physics'])} {random.choice(['Community', 'Group', 'Enthusiasts', 'Experts'])}"
    username = f"{random.choice(['User', 'Coder', 'Dev', 'Pro', 'Guru', 'Master', 'Ninja', 'Geek', 'Techie', 'Hacker'])}{random.randint(1, 1000)}"
    content_type = random.choice(content_types)
    data.append([content_name, content_type, community_name, username])

# Create a DataFrame
df = pd.DataFrame(data, columns=fields)

# Save to Excel
df.to_excel("content_dataset.xlsx", index=False)