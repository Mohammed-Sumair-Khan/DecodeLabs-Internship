# Simple Recommendation System
# Based on user preferences

items = [
    {
        "name": "The Dark Knight",
        "category": "movie",
        "genres": ["action", "thriller", "crime"]
    },
    {
        "name": "Inception",
        "category": "movie",
        "genres": ["action", "sci-fi", "thriller"]
    },
    {
        "name": "Interstellar",
        "category": "movie",
        "genres": ["sci-fi", "drama", "adventure"]
    },
    {
        "name": "Friends",
        "category": "series",
        "genres": ["comedy", "romance"]
    },
    {
        "name": "Breaking Bad",
        "category": "series",
        "genres": ["crime", "drama", "thriller"]
    },
    {
        "name": "Stranger Things",
        "category": "series",
        "genres": ["sci-fi", "horror", "adventure"]
    },
    {
        "name": "The Office",
        "category": "series",
        "genres": ["comedy"]
    }
]


def recommend(preferences):
    recommendations = []

    for item in items:
        score = 0

        # Check preferred category
        if preferences["category"] == item["category"]:
            score += 2

        # Check preferred genres
        for genre in preferences["genres"]:
            if genre in item["genres"]:
                score += 1

        if score > 0:
            recommendations.append((item["name"], score))

    # Sort by highest matching score
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations


print("===== Recommendation System =====")

category = input(
    "What do you prefer? (movie/series): "
).strip().lower()

genre_input = input(
    "Enter your favorite genres separated by commas "
    "(e.g. action, thriller): "
).strip().lower()

genres = [genre.strip() for genre in genre_input.split(",")]

preferences = {
    "category": category,
    "genres": genres
}

results = recommend(preferences)

print("\n===== Recommended Items =====")

if results:
    for name, score in results:
        print(f"{name} - Match Score: {score}")
else:
    print("Sorry, no matching recommendations found.")