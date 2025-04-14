from flask import Flask, render_template
import pandas as pd 

# DATA!!

# ***************** CHARACTERS!! ***************** 
npc_df = pd.read_csv('characters.csv')
npc_ver2_df = pd.read_csv('villagers.csv')

# Add the 'Giftable' column from npc_ver2_df to npc_df, based on the Name of each npc
npc_df = npc_df.merge(npc_ver2_df[['Name', 'Giftable']], on='Name', how='left')
print(npc_df.info())

giftable_npcs = npc_df['Giftable'] = True; 
non_giftable_npcs = npc_df['Giftable'] = False; 


# ***************** ABANDONED HOUSE!! ***************** 
abandoned_house_hats_df = pd.read_csv('abandonedhousehats - Sheet1.csv')
print(abandoned_house_hats_df.info())



# ***************** ACHIEVEMENTS!!  ***************** 
achievements_df = pd.read_csv('Achievements - Sheet1.csv')
print(achievements_df.head())
 

# ***************** CROPS!! ***************** 
crops_df = pd.read_csv('crops.csv')


app = Flask(__name__)

# **************** ROUTES ******************
# Home
@app.route("/")
@app.route("/home/")
def index():
    return render_template('index.html')

# NPCS
@app.route('/routes/npc_routes/<route_type>')
def npcroute(route_type): 
    return render_template(f'routes/npc_routes/{route_type}.html', route_type=route_type)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 1234, debug=True)

