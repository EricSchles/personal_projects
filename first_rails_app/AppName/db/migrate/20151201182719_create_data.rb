class CreateData < ActiveRecord::Migration
  def change
    create_table :data do |t|
      t.string :data, default: "no data"
      t.timestamps null: false
    end
  end
end
