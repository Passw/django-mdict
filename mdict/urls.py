from django.urls import re_path
from django.urls import path

from . import views

app_name = 'mdict'
urlpatterns = [
    path('', views.mdict_index),
    path('sug/', views.search_suggestion),
    re_path(r'^(\d+)/(.+)/$', views.search_mdd),
    re_path(r'^(\d+)/(.+)$', views.search_mdd),
    re_path(r'^dic/(\d+)/$', views.mdict_dic),
    re_path(r'^dic/(\d+)/(.+)$', views.search_mdd),
    re_path(r'^es/(\d+)/(.+)$', views.search_mdd),
    re_path(r'^esdic/(\d+)/(.+)$', views.search_mdd),
    re_path(r'^shelf/(\d+)/(.+)$', views.search_mdd),
    re_path(r'^shelf2/(\d+)/(.+)$', views.search_mdd),
    re_path(r'^shelf3/(\d+)/(.+)$', views.search_mdd),
    path('getexfile/', views.get_external_file),
    re_path('getexfile/(.+)', views.get_external_file),
    path('es/getexfile/', views.get_external_file),
    re_path('es/getexfile/(.+)', views.get_external_file),
    path('audio/', views.search_audio),
    path('key/', views.search_mdx_key),
    path('record/', views.search_mdx_record),
    path('getentrylist/', views.get_entry_list),
    path('getlbocknum/', views.get_block_num),
    path('getmdictlist/', views.get_mdict_list),
    path('getdicinfo/', views.get_dic_info),
    path('getdicgroup/', views.get_dic_group),
    path('setmdictenable/', views.set_mdict_enable),
    path('retrieveconfig/', views.retrieve_config),
    path('saveconfig/', views.save_config),
    path('bujian/', views.bujianjiansuo),
    path('es/', views.es_index),
    path('essearch/', views.fulltext_search),
    path('initindex/', views.init_index),
    path('indexstatus/', views.get_index_status),
    path('downloadhistory/', views.download_history),
    path('wordcloud/', views.wordcloud),
    path('getwordlist/', views.getwordlist),
    re_path(r'^esdic/(\d+)/$', views.es_dic),
    re_path(r'^zim/(\d+)/(.+)$', views.search_zim),
    re_path(r'^dic/zim/(\d+)/(.+)$', views.search_zim),
    re_path(r'^es/zim/(\d+)/(.+)$', views.search_zim),
    re_path(r'^zim/$', views.search_zim_dic),
    path('randomsearch/', views.random_search),
    path('getpkingroup/', views.get_pk_in_group),
    path('editdic/', views.edit_dic),
    path('getprior/', views.get_prior),
    path('shelf/', views.shelf),
    path('shelf2/', views.shelf2),
    path('shelf3/', views.shelf3),
    path('doc/', views.doc),
    re_path('doc/(.+)', views.doc_md),
    path('addtogroup/', views.add_to_group),
    path('deleteitem/', views.delete_item),
    path('renameitem/', views.rename_item),
    path('moveitem/', views.move_item),
    path('grouping/', views.grouping),
    path('grouping/mdictpath/', views.grouping_mdictpath),
    path('grouping/mdictgroup/', views.grouping_mdictgroup),
    path('grouping/creategroup/', views.create_group),
    path('openpath/', views.open_path),
    path('createdeck/', views.create_anki_deck),
    path('deckgroup/', views.deck_group),
    path('addtodeck/', views.add_to_deck),
    path('characters/', views.characters),
    path('network/', views.network),
    path('getnodes/', views.get_nodes),
    path('getmymdictentry/', views.get_mymdictentry),
    path('getnodeid/', views.get_node_id),
    path('addnode/', views.add_node),
    path('addedge/', views.add_edge),
    path('editedge/', views.edit_edge),
    path('getlabels/', views.get_labels),
]
