
class Solutions:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Сложность алгоритма:
        По времени: O(n+m)
        По памяти: O(1) (кроме входных данных и выходого больше ничего не используем)
        :param word1: Первая строка
        :param word2: Вторая строка
        :return: Строка, полученная путем объединения символов двух строк поочередно.
        """
        max_len = max(len(word1), len(word2))
        res = []
        for i in range(max_len):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return ''.join(res)
