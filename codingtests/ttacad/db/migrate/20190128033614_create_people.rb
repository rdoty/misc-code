class CreatePeople < ActiveRecord::Migration[5.2]
  def change
    create_table :people do |t|
      t.numeric :height
      t.numeric :weight

      t.timestamps
    end
  end
end
