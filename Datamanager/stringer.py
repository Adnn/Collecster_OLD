from collections import deque
import os

def get_remaining_count(queue):
    count = len(queue) - 1 #count the whitespaces
    for word in queue:
        count += len(word)

    return count

def balance_string(text, max_lines, min_cols):
    
    words_queue = deque(text.split(' '))
    return append_line(words_queue, max_lines, min_cols)


def append_line(words_queue, remaining_lines, min_cols):
    if (len(words_queue) == 0):
        return ''

    remaining_lines -= 1
    current_line = words_queue.popleft()

    while (len(words_queue)):
        potential_length = len(current_line)+len(words_queue[0])
        
        if( (remaining_lines==0) or (potential_length < min_cols) or (potential_length < (get_remaining_count(words_queue)//remaining_lines)) ):
            current_line += ' '+words_queue.popleft()
        else:
            min_cols = max(min_cols, len(current_line))
            return current_line + os.linesep + append_line(words_queue, remaining_lines, min_cols)

    return current_line
