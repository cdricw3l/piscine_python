# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/15 03:07:50 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/15 03:13:08 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
    def recusive_count(start: int, end: int):
        if(start > end):
            return 
        print("Day", start)
        recusive_count(start + 1, end)
    i = input("Days until harvest: ")
    recusive_count(1, int(i))
    
    