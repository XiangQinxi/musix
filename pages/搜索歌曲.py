import streamlit as st

st.set_page_config(
    page_title="Musix-Search",
    page_icon="🎶",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None
)

st.header("Musix")

st.subheader("搜索歌曲")

search_name = st.text_input("搜索歌曲名称", placeholder="e.g. ”Hopes and Dreams“")

with st.expander("高级选项"):
    search_numbers = st.slider("最大搜索量", value=10, step=1, min_value=0, max_value=500, help="搜索量过大，可能会造成卡顿")

with st.container():
    search_start = st.button("开始搜索", use_container_width=True)
    if search_start and search_name != "":
        import cloudmusic

        results = cloudmusic.search(search_name, number=search_numbers)

        for music in results:
            with st.expander(music.name+" - "+', '.join("{0}".format(x) for x in music.artist), True):
                st.caption("Music ID : "+music.id)
                st.caption("Music Url : " + str(music.url))
                st.caption("Music Size : "+str(music.size)+"byte")
                st.caption("Music Type : "+music.type)
                st.caption("Music Level : "+music.level)

                import urllib, os.path

                resp = urllib.request.urlopen(music.url, timeout=5)
                respHtml = resp.read()

                if len(music.artist) == 1:
                    artist = music.artist[0]
                else:
                    artist = ""
                    for ar in music.artist:
                        artist += ar + " "
                name = music.name + " - " + artist + "." + music.type

                st.audio(respHtml)

                if st.download_button("下载", key=music.id, data=respHtml, use_container_width=True, file_name=music.name+" - "+', '.join("{0}".format(x) for x in music.artist)+"."+music.type):
                    music.download(level="lossless")

        st.success("搜索完毕！")