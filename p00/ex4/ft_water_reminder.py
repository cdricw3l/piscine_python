# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/15 02:58:44 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/15 03:00:21 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    i = input("Days since last watering: ")
    if(int(i) > 2):
        print("Water the plants!")
    elif(int(i) <= 2):
        print("Plants are fine")