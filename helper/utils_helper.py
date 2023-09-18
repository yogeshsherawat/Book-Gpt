from sklearn.metrics.pairwise import cosine_similarity


class UtilsHelper(object):


    @staticmethod
    def find_k_closest_to_given_vector(target_vector, documents):
        similarities = []
        for doc in documents:
            similarity = cosine_similarity([target_vector], [doc[1]])[0][0]
            similarities.append((doc[0], similarity))

        # Sort the documents by similarity (higher values are closer)
        similarities.sort(key=lambda x: x[1], reverse=True)

        # Number of closest neighbors to retrieve
        K = 10  # Change to your desired value

        # Get the top K closest neighbors
        closest_neighbors = similarities[:K]

        return closest_neighbors
