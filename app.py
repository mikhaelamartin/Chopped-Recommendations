import streamlit as st 
import pickle
import pandas as pd 

episode_list = pickle.load(open('episodes.pkl','rb'))
chopped = pd.DataFrame(episode_list)
cosine_sim = pickle.load(open('cosine_sim.pkl','rb'))


# create function to print names of similar episodes
def get_names(episode_name):
    enumerated = enumerate(cosine_sim[chopped[chopped['episode_name'] == episode_name].index[0]])
    listed = list(enumerated)
    sorteds = sorted(listed,key = lambda x:x[1], reverse=True)[:10] 
    names = []
    for i in sorteds[1:]:
        episode = 'Episode '+ str(i[0]+1)+ ': ' + str(chopped.iloc[i[0]].episode_name)
        names.append(episode)     
    return names


st.title('Chopped Episodes Recommendations')

option = st.selectbox('Find episodes similar to: ', chopped['episode_name'].values)

if st.button('Recommend'):
	for i in get_names(option):
		st.write(i)