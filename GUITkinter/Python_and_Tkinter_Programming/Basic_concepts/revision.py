dict = {1 : [1,2,3], 2: [4,5,6], 3 : [7,8,9]}

usr_ans = dict.get(2,None)

def correct_pronouns():
    pass
    return

#basically, have each figure of speech as a function and move
def correct_articles():
    pass
    return
#proper_nouns_list = []
#adjectives_list = []
def correct_base(ans):
    acid_bases_list = []
    ans_list = []
    if ans in acid_bases_list:
        ans_mark_percentage = 0
        question_total = 4
        ans_mark_percentage = ans / question_total
        ans_list.insert(ans_mark)
        #print("correct")/ use a tick image & only print final mark of assessment
    return ans_list

    #if usr_ans == correct_ans:
    #display next question if they in a test/ assigment
    #display feedback if they in a tutorial/class
#To track student marks, we'll keep their score count in a list, and add & loop that shit.
def tutorial_total(ans_list):
    tut_sum = 0
    for tut_total in ans_list:
        tut_sum += tut_total
        return tut_sum
def exam_entrance_mark_composition(tut_sum, project_sum, tests_sum):
    exam_entry_mark = sum(tut_sum, project_sum, tests_sum)
    return exam_entry_mark

def final_mark(exam_result,exam_entrance):
    final_result = sum(exam_result,exam_entrance)
    return final_result