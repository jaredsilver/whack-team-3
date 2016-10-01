class CreateGoalTypes < ActiveRecord::Migration[5.0]
  def change
    create_table :goal_types do |t|
      t.string :name
      t.string :unit

      t.timestamps
    end
  end
end
