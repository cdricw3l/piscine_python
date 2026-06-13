# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    _init_.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/15 02:17:37 by cdric.b           #+#    #+#              #
#    Updated: 2026/03/15 05:04:32 by cdric.b          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from ex00.ft_hello_garden import *
from ex1.ft_plot_area import *
from ex2.ft_harvest_total import *
from ex3.ft_plant_age import *
from ex4.ft_water_reminder import *
from ex5.ft_count_harvest_iterative import *
from ex5.ft_count_harvest_recursive import *
from ex6.ft_garden_summary import *
from ex7.ft_seed_inventory import *

def main():
    try:
        i = sys.argv[1]
    except:
        i = input("Run fonction: ")
    match i:
        case "0":
            ft_hello_garden()
        case "1":
            ft_plot_area()
        case "2":
            ft_harvest_total()
        case "3":
            ft_plant_age()
        case "4":
            ft_water_reminder()
        case "50":
            ft_count_harvest_iterative()
        case "51":
            ft_count_harvest_recursive()
        case "6":
            ft_garden_summary()
        case "7":
            ft_seed_inventory("tomato", 15, "packets")
            ft_seed_inventory("carrot", 8, "grams")
            ft_seed_inventory("lettuce", 12, "area")
            ft_seed_inventory("lettuce", 12, "hello")

main()