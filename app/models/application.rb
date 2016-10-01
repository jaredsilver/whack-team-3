class Application < ApplicationRecord

  def add_goal(user_id, goal_type_id, quantity)
    goal = Goal.new
    goal.user = User.find(user_id)
    goal.goal_type = GoalType.find(goal_type_id)
    goal.quantity = quantity
    goal.save
  end

end
