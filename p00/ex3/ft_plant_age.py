# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/15 02:26:36 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/15 02:48:52 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    i = input("Enter plant age in days: ")
    if (int(i) > 60):
        print("Plant is ready to harvest!")
    elif(int(i) < 60):
        print("Plant needs more time to grow.")