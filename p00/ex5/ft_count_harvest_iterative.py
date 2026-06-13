# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/15 03:04:17 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/15 03:07:13 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    i = input("Days until harvest: ")
    j = 1
    while (j <= int(i)):
        print("Day", j)
        j += 1