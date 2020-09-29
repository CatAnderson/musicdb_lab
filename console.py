import pdb
from models.artist import Artist
import repositories.artist_repository as artist_repository

artist1 = Artist("Prodigy")
artist_repository.save(artist1)
artist2 = Artist("Nick Cave")
artist_repository.save(artist2)
artist3 = Artist("BackStreetBoys")
artist_repository.save(artist3)

artists = artist_repository.select_all()


pdb.set_trace()
