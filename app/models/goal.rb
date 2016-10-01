class Goal < ApplicationRecord
  belongs_to :goal_type, dependent: :destroy
  belongs_to :user, dependent: :destroy

  validates :goal_type, presence: true
  validates :user, presence: true

end
