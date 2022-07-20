bl_info = {
    "name": "Axis Lock and Reset",
    "author": "Arnold",
    "version": (0,8),
    "blender": (3, 2, 0),
    "location": "View3D > Tool",
    "description": "Locks and clears rotation on a singular axis",
    "warning": "",
    "wiki_url": "",
    "category": "Animation",
}






import bpy

class PosX(bpy.types.Operator):
    """Tooltip"""
    bl_label = "PosX"
    bl_idname = "object.position_button_x"
    
    def execute(self, context):
        for b in bpy.context.selected_pose_bones:
            if(b.lock_location[0] == True):
                b.lock_location[0] = False
            else:
                b.lock_location[0] = True
            
        return {'FINISHED'}
    
    
class PosY(bpy.types.Operator):
    """Tooltip"""
    bl_label = "PosY"
    bl_idname = "object.position_button_y"
    
    def execute(self, context):
        for b in bpy.context.selected_pose_bones:
            if(b.lock_location[1] == True):
                b.lock_location[1] = False
            else:
                b.lock_location[1] = True
            
        return {'FINISHED'}
    
    
class PosZ(bpy.types.Operator):
    """Tooltip"""
    bl_label = "PosZ"
    bl_idname = "object.position_button_z"
    
    def execute(self, context):
        for b in bpy.context.selected_pose_bones:
            if(b.lock_location[2] == True):
                b.lock_location[2] = False
            else:
                b.lock_location[2] = True
            
        return {'FINISHED'}
        
class ResetX(bpy.types.Operator):
    """Tooltip"""
    bl_label = "ResetX"
    bl_idname = "object.reset_x"
    
    def execute (self,context):
        for b in bpy.context.selected_pose_bones:
            if b.rotation_mode == 'QUATERNION':
                b.rotation_quaternion[1] = 0.0
            elif b.rotation_mode == 'XYZ':
                b.rotation_euler[0] = 0.0
        return {'FINISHED'}
    
    
    
class ResetY(bpy.types.Operator):
    """Tooltip"""
    bl_label = "ResetZ"
    bl_idname = "object.reset_y"
    
    def execute (self,context):
        for b in bpy.context.selected_pose_bones:
            if b.rotation_mode == 'QUATERNION':
                b.rotation_quaternion[2] = 0.0
            elif b.rotation_mode == 'XYZ':
                b.rotation_euler[1] = 0.0
        return {'FINISHED'}
    
    
class ResetZ(bpy.types.Operator):
    """Tooltip"""
    bl_label = "ResetZ"
    bl_idname = "object.reset_z"
    
    def execute (self,context):
        for b in bpy.context.selected_pose_bones:
            if b.rotation_mode == 'QUATERNION':
                b.rotation_quaternion[3] = 0.0
            elif b.rotation_mode == 'XYZ':
                b.rotation_euler[2] = 0.0
        return {'FINISHED'}

class ExecY(bpy.types.Operator):
    """Tooltip"""
    bl_label = "ExecY"
    bl_idname = "object.button_y"
    
    def execute(self, context):
        for b in bpy.context.selected_pose_bones:
            if(b.lock_rotation[1] == True):
                b.lock_rotation[1] = False
            else:
                b.lock_rotation[1] = True
            
        return {'FINISHED'}

class ExecX(bpy.types.Operator):
    """Tooltip"""
    bl_label = "ExecX"
    bl_idname = "object.button_x"
    
    def execute(self, context):
        for b in bpy.context.selected_pose_bones:
            if(b.lock_rotation[0] == True):
                b.lock_rotation[0] = False
            else:
                b.lock_rotation[0] = True
            
        return {'FINISHED'}
    
    
class ExecZ(bpy.types.Operator):
    """Tooltip"""
    bl_label = "ExecZ"
    bl_idname = "object.button_z"
    
    def execute(self, context):
        for b in bpy.context.selected_pose_bones:
            if(b.lock_rotation[2] == True):
                b.lock_rotation[2] = False
            else:
                b.lock_rotation[2] = True
            
        return {'FINISHED'}

class Test(bpy.types.Panel):
    bl_label = "Test"
    bl_idname = "PT_Test"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Axes Locker'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        
        
        row.label(text="Rotation Locking", icon='LOCKED')
        row = layout.row()
        row.operator("object.button_x", text = "Unlock/Lock X Rotation")
        row = layout.row()
        row.operator("object.button_y", text = "Unlock/Lock Y Rotation")
        row = layout.row()
        row.operator("object.button_z", text = "Unlock/Lock Z Rotation")
        
        row = layout.row()
        row.label(text="Location Locking", icon='LOCKED')
        row = layout.row()
        row.operator("object.position_button_x", text ="Unlock/Lock X Location")
        row = layout.row()
        row.operator("object.position_button_y", text ="Unlock/Lock Y Location")
        row = layout.row()
        row.operator("object.position_button_z", text ="Unlock/Lock Z Location")
        row = layout.row()
        
        row = layout.row()
        row.label(text="Rotation Clearing", icon='DRIVER_ROTATIONAL_DIFFERENCE')
        row = layout.row()
        row.operator("object.reset_x", text = "Clear X Rotation")
        row = layout.row()
        row.operator("object.reset_y", text = "Clear Y Rotation")
        row = layout.row()
        row.operator("object.reset_z", text = "Clear Z Rotation")
        

classes = [Test,ExecX,ExecY,ExecZ,ResetX,ResetY,ResetZ,PosX,PosY,PosZ]

       
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()