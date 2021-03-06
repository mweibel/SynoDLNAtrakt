from sqlalchemy import create_engine, MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine('postgresql+pg8000://admin@localhost/mediaserver', encoding='utf-8', convert_unicode=True, echo=False)
metadata = MetaData()

Base = declarative_base()


# CREATE TABLE video
# (
#   id serial NOT NULL,
#   path text NOT NULL,
#   title text NOT NULL,
#   filesize int8 NOT NULL DEFAULT 0,
#   album text,
#   container_type text NOT NULL,
#   video_codec text,
#   frame_bitrate int4,
#   frame_rate_num int4,
#   frame_rate_den int4,
#   video_bitrate int4,
#   video_profile int4,
#   video_level int4,
#   resolutionX int4,
#   resolutionY int4,
#   audio_codec text,
#   audio_bitrate int4,
#   frequency int4,
#   channel int4,
#   duration int4,
#   date timestamp,
#   mdate timestamp,
#   fs_uuid text,
#   fs_online boolean DEFAULT TRUE,
#   CONSTRAINT video_pkey PRIMARY KEY (id)
# )

class Video(Base):
	__tablename__ = 'video'

	id = Column(Integer, primary_key=True)
	path = Column(String)
	title = Column(String)
	filesize = Column(Integer)
	# album = Column(String)
	# container_type = Column(String)
	# video_codec = Column(String)
	# frame_bitrate = Column(Integer)
	# frame_rate_num = Column(Integer)
	# frame_rate_den = Column(Integer)
	# video_bitrate = Column(Integer)
	# video_profile = Column(Integer)
	# video_level = Column(Integer)
	# resolutionX = Column(Integer)
	# resolutionY = Column(Integer)
	# audio_codec = Column(String)
	# audio_bitrate = Column(Integer)
	# frequency = Column(Integer)
	# channel = Column(Integer)
	duration = Column(Integer)
	date = Column(Integer)
	mdate = Column(Integer)
	# fs_uuid = Column(Integer)
	# fs_online = Column(Integer)


	def __init__(self, path, duration, date, mdate, title, filesize):
		self.path = path
		self.duration = duration
		self.date = date
		self.mdate = mdate
		self.title = title
		self.filesize = filesize

	def __repr__(self):
		return u"<Video(id:{0}, path:{1}, duration:{2}, data:{3}, mdate:{4}, title:{5}, filesize:{6} )>".format(self.id, self.path, self.duration, self.date, self.mdate, self.title, self.filesize)


Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = scoped_session(Session)
