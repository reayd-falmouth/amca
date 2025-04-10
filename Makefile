NUM := 10

# Check-in code after formatting
checkin: ## Perform a check-in after formatting the code
    ifndef COMMIT_MESSAGE
		$(eval COMMIT_MESSAGE := $(shell bash -c 'read -e -p "Commit message: " var; echo $$var'))
    endif
	@git add --all; \
	  git commit -m "$(COMMIT_MESSAGE)"; \
	  git push

play_rl:
	@poetry run python play.py

play_sarsa:
	@poetry run python sarsa_play.py

train_rl:
	@poetry run python train.py -e $(NUM)


train_sarsa:
	@echo "Started at: $$(date)"
	@start=$$(date +%s); \
	poetry run python sarsa_train.py --games $(NUM) --name amca/models/sarsa-vs_random.pkl; \
	end=$$(date +%s); \
	echo "Ended at: $$(date)"; \
	duration=$$((end - start)); \
	echo "Total time: $${duration}s"; \
	echo "Time per game: $$(echo "scale=4; $$duration / $(NUM)" | bc)s"
