#Bài 1. In ra thông báo
#print("Hello world!")

# Bài 2. Cho xâu s = "Việc học tập là rất quan trọng, cho nên, cần học, học nữa, học mãi".
# 1/ Xác định từ với tần số xuất hiện nhiều nhất, nếu có nhiều từ có cùng tần số nhiều nhất, in ra tất cả các từ đó (cùng với tần số của nó).
# 2/ Xác định độ dài của mỗi từ trong câu (không quan tâm đến lặp lại).
# 3/ Cho một bộ từ điển gồm các từ {học, nữa, học sinh, học bạ, mãi, học tập}, hãy xác định các từ xuất hiện trong bộ từ điển nói trên.

s = "Việc học tập là rất quan trọng, cho nên, cần học, học nữa, học mãi"

#1/ 
def most_frequent_word(s): 
    clean = s.lower().translate(str.maketrans('', '', ',.'))
    words = clean.split()
    words_dict = {}
    result_dict = {}
    
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        if word not in words_dict: 
            words_dict[word] = 1

    print(words_dict)
    a = max(words_dict.values())
    for word, frequency in words_dict.items():
        if frequency == a:
            result_dict[word] = frequency
    return result_dict
        
#print("Từ xuất hiện nhiều nhất là:", most_frequent_word(s))


#2/

def determine_length(s):
    clean = s.lower().translate(str.maketrans('', '', ',.'))
    words = clean.split()
    word_dict = {}
    
    for word in words:
        word_dict[word] = len(word)
    return word_dict

#print("Độ dài các từ là: ", determine_length(s))


#3/
dictionary = {"học", "nữa", "học sinh", "học bạ", "mãi", "học tập"}
def is_in_dictionary(s, dictionary):
    clean = s.lower().translate(str.maketrans("", '', ',.'))
    already_print = []
    for value in dictionary:
        if value in clean and value not in already_print:
            print(value, " có trong từ điển")
            already_print.append(value)

is_in_dictionary(s, dictionary)                
            