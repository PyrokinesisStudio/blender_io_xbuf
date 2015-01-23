# This file is part of external_render_engine.  external_render_engine is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright David Bernard

# <pep8 compliant>

from . import renderengine
from . import protocol
from . import pgex_export
from . import helpers

__all__ = ['renderengine', 'protocol', 'helpers', 'pgex_export']

bl_info = {
    "name": "External Render Engine",
    "author": "David Bernard",
    "version": (0, 3),
    "blender": (2, 72, 0),
    "location": "Render > Engine > External Render",
    "description": "Delegate rendering to an external render engine (eg provided by game engine)",
    "warning": "This script is Alpha",
    "wiki_url": "https://github.com/davidB/blender_external_renderer",
    "tracker_url": "https://github.com/davidB/blender_external_renderer/issues",
    "category": "Render"}

import bpy


class RenderSettingsScene(bpy.types.PropertyGroup):

    port = bpy.props.IntProperty(
        name="port",
        description="",
        default=4242, min=1024)
    host = bpy.props.StringProperty(
        name="host",
        description="",
        default="127.0.0.1")

    def __init__(self):
        pass


class PgexSettingsScene(bpy.types.PropertyGroup):

    assets_path = bpy.props.StringProperty(
        name="assets root folder path",
        description="Full path to directory where the assets are saved",
        maxlen=1024, subtype="DIR_PATH")

    def __init__(self):
        pass


class ExternalRenderPanel(bpy.types.Panel):
    bl_idname = "RENDER_PT_external_render"
    bl_label = "External Render Config"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_options = {'DEFAULT_CLOSED'}
    COMPAT_ENGINES = {renderengine.ExternalRenderEngine.bl_idname}

    def __init__(self):
        pass

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return engine in cls.COMPAT_ENGINES

    def draw(self, context):
        layout = self.layout
        render = context.scene.external_render
        pgex = context.scene.pgex
        row = layout.row()
        row.prop(render, "host")
        row.prop(render, "port")
        col = layout.column()
        col.prop(pgex, "assets_path")
        # layout.label(text="Hello World")


def register_settings():
    bpy.utils.register_class(RenderSettingsScene)
    bpy.types.Scene.external_render = bpy.props.PointerProperty(type=RenderSettingsScene)
    bpy.utils.register_class(PgexSettingsScene)
    bpy.types.Scene.pgex = bpy.props.PointerProperty(type=PgexSettingsScene)
    bpy.utils.register_class(ExternalRenderPanel)


def unregister_settings():
    bpy.utils.unregister_class(ExternalRenderPanel)
    # del bpy.types.Scene.pgex
    bpy.utils.unregister_class(PgexSettingsScene)
    # del bpy.types.Scene.external_renderer
    bpy.utils.unregister_class(RenderSettingsScene)


def register_renderer():

    # Register the RenderEngine
    bpy.utils.register_class(renderengine.ExternalRenderEngine)

    # RenderEngines also need to tell UI Panels that they are compatible
    # Otherwise most of the UI will be empty when the engine is selected.
    # In this example, we need to see the main render image button and
    # the material preview panel.
    import bl_ui
    panels = [
        bl_ui.properties_render.RENDER_PT_render,
        # bl_ui.properties_material.MATERIAL_PT_preview,
        bl_ui.properties_material.MATERIAL_PT_context_material,
        bl_ui.properties_material.MATERIAL_PT_diffuse,
        bl_ui.properties_material.MATERIAL_PT_specular,
        bl_ui.properties_material.MATERIAL_PT_shadow,
        bl_ui.properties_material.MATERIAL_PT_shading,
        bl_ui.properties_material.MATERIAL_PT_custom_props,
        bl_ui.properties_data_lamp.DATA_PT_lamp,
        bl_ui.properties_data_lamp.DATA_PT_spot,
        bl_ui.properties_data_lamp.DATA_PT_custom_props_lamp,
    ]
    for p in panels:
        p.COMPAT_ENGINES.add(renderengine.ExternalRenderEngine.bl_idname)


def unregister_renderer():
    bpy.utils.unregister_class(renderengine.ExternalRenderEngine)


def menu_func_exporter(self, context):
    self.layout.operator(pgex_export.PgexExporter.bl_idname, text="Pgex (.pgex)")


def register_exporter():
    bpy.utils.register_class(pgex_export.PgexExporter)
    bpy.types.INFO_MT_file_export.append(menu_func_exporter)


def unregister_exporter():
    bpy.types.INFO_MT_file_export.remove(menu_func_exporter)
    bpy.utils.unregister_class(pgex_export.PgexExporter)


def register():
    register_settings()
    register_exporter()
    register_renderer()


def unregister():
    unregister_renderer()
    unregister_exporter()
    unregister_settings()


def main():
    try:
        unregister()
    except (RuntimeError, ValueError):
        pass
    register()


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    main()
