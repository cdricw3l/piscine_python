# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/15 02:22:06 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/15 02:48:51 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    i = input("Day 1 harvest: ")
    j = input("Day 2 harvest: ")
    k = input("Day 3 harvest: ")
    print("Total harvest:",(int(i) + int(j) + int(k)))