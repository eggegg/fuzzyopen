from gi.repository import GObject, Gedit
from fuzzyopen import FuzzyOpenPluginInstance
from config import FuzzyOpenConfigWindow

# STANDARD PLUMMING
class FuzzyOpenPlugin( GObject.Object, Gedit.WindowActivatable ):
  __gtype_name__ = "FuzzyOpenPlugin"

  DATA_TAG = "FuzzyOpenPluginInstance"
  window = GObject.property(type=Gedit.Window)

  def __init__( self ):
    GObject.Object.__init__( self )

  def _get_instance( self ):
    return self.window.get_data( self.DATA_TAG )

  def _set_instance( self, instance ):
    self.window.set_data( self.DATA_TAG, instance )

  def is_configurable( self ):
    return True

  def create_configure_dialog( self ):
    return FuzzyOpenConfigWindow()._window

  def activate( self ):
    self._set_instance( FuzzyOpenPluginInstance( self ) )

  def deactivate( self ):
    self._get_instance( ).deactivate()
    self._set_instance( None )

  def update_ui( self ):
    self._get_instance( ).update_ui()

