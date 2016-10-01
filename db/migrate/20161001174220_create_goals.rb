class CreateGoals < ActiveRecord::Migration[5.0]
  def change
    create_table :goals do |t|
      t.references :user
      t.references :goal_type
      t.integer :quantity

      t.timestamps
    end
  end
end
