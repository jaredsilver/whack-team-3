class Goal < ApplicationRecord
  belongs_to :goal_type, dependent: :destroy
  belongs_to :user, dependent: :destroy 
end
