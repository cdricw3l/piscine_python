# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/15 04:52:39 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/15 05:04:19 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if(unit == "packets"):
        print(seed_type.capitalize(),"seeds:", quantity, unit, "available")
    elif(unit == "grams"):
        print(seed_type.capitalize(), "seeds:", quantity, unit, "total")
    elif(unit == "area"):
        print(seed_type.capitalize(), "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")

        
    