INTERPRETER= python3
EX=0
git:
	git add .
	git commit -m python_03/ex$(EX)
	git push origin $(shell git branch --show-current)

EX0= ft_command_quest.py 
EX1= ft_score_analytics.py 
EX2= ft_coordinate_system.py 
EX3= ft_achievement_tracker.py 
EX4= ft_inventory_system.py 
EX5= ft_data_stream.py 
EX6= ft_data_alchemist.py 
ARG=
ex0:
	@$(INTERPRETER) ex0/$(EX0) $(ARG)
ex1:
	@$(INTERPRETER) ex1/$(EX1) $(ARG)
ex2:
	@$(INTERPRETER) ex2/$(EX2) $(ARG)
ex3:
	@$(INTERPRETER) ex3/$(EX3) $(ARG)
ex4:
	@$(INTERPRETER) ex4/$(EX4)  sword:1 potion:5 shield:2 armor:3 helmet:1 sword:1 hello key:value
ex5:
	@$(INTERPRETER) ex5/$(EX5) $(ARG)
ex6:
	@$(INTERPRETER) ex6/$(EX6) $(ARG)

.PHONY: ex0 ex1 ex2 ex3 ex4 ex5 ex6