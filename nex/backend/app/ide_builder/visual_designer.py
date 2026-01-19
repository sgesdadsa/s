"""
NEX Visual Forms Designer
Drag-and-drop form designer for WinForms, WPF, and Web
AI-powered form generation and improvement
"""

from typing import Dict, List, Any, Optional
from pathlib import Path
import json

class VisualFormsDesigner:
    """
    Visual designer for creating forms
    Supports: WinForms (C#, VB.NET), WPF, Web Forms
    """

    def __init__(self):
        self.forms = {}
        self.components = self._init_components()

    def _init_components(self) -> Dict[str, Any]:
        """Initialize available components"""
        return {
            'controls': {
                'Button': {
                    'properties': ['Text', 'Size', 'Location', 'BackColor', 'Font'],
                    'events': ['Click', 'MouseEnter', 'MouseLeave'],
                    'category': 'Basic'
                },
                'TextBox': {
                    'properties': ['Text', 'Size', 'Location', 'Multiline', 'ReadOnly'],
                    'events': ['TextChanged', 'KeyPress', 'KeyDown'],
                    'category': 'Basic'
                },
                'Label': {
                    'properties': ['Text', 'Size', 'Location', 'Font', 'ForeColor'],
                    'events': ['Click'],
                    'category': 'Basic'
                },
                'ComboBox': {
                    'properties': ['Items', 'SelectedIndex', 'Size', 'Location'],
                    'events': ['SelectedIndexChanged'],
                    'category': 'Basic'
                },
                'ListBox': {
                    'properties': ['Items', 'SelectedIndex', 'Size', 'Location'],
                    'events': ['SelectedIndexChanged'],
                    'category': 'Basic'
                },
                'CheckBox': {
                    'properties': ['Text', 'Checked', 'Size', 'Location'],
                    'events': ['CheckedChanged'],
                    'category': 'Basic'
                },
                'RadioButton': {
                    'properties': ['Text', 'Checked', 'Size', 'Location'],
                    'events': ['CheckedChanged'],
                    'category': 'Basic'
                },
                'DataGridView': {
                    'properties': ['Columns', 'DataSource', 'Size', 'Location'],
                    'events': ['CellClick', 'SelectionChanged'],
                    'category': 'Data'
                },
                'MenuStrip': {
                    'properties': ['Items', 'Location'],
                    'events': ['ItemClicked'],
                    'category': 'Menus'
                },
                'Panel': {
                    'properties': ['Size', 'Location', 'BorderStyle', 'BackColor'],
                    'events': ['Click'],
                    'category': 'Containers'
                },
                'TabControl': {
                    'properties': ['TabPages', 'SelectedIndex', 'Size', 'Location'],
                    'events': ['SelectedIndexChanged'],
                    'category': 'Containers'
                }
            }
        }

    # ==================== FORM CREATION ====================

    async def create_form(self, form_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create new form
        """
        form_id = self._generate_form_id()

        form = {
            'id': form_id,
            'name': form_data.get('name', 'Form1'),
            'title': form_data.get('title', 'My Form'),
            'size': form_data.get('size', {'width': 800, 'height': 600}),
            'type': form_data.get('type', 'winforms'),  # winforms, wpf, web
            'language': form_data.get('language', 'csharp'),
            'controls': [],
            'properties': {},
            'events': {}
        }

        self.forms[form_id] = form
        return form

    async def add_control(self, form_id: str, control_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add control to form
        """
        if form_id not in self.forms:
            return {'success': False, 'error': 'Form not found'}

        form = self.forms[form_id]

        control = {
            'id': self._generate_control_id(),
            'type': control_data.get('type', 'Button'),
            'name': control_data.get('name', f"{control_data.get('type', 'Button')}1"),
            'properties': control_data.get('properties', {}),
            'events': control_data.get('events', {}),
            'position': control_data.get('position', {'x': 0, 'y': 0}),
            'size': control_data.get('size', {'width': 100, 'height': 30})
        }

        form['controls'].append(control)

        return {
            'success': True,
            'control': control
        }

    async def update_control(self, form_id: str, control_id: str, updates: Dict[str, Any]):
        """Update control properties"""
        if form_id not in self.forms:
            return {'success': False, 'error': 'Form not found'}

        form = self.forms[form_id]
        control = next((c for c in form['controls'] if c['id'] == control_id), None)

        if not control:
            return {'success': False, 'error': 'Control not found'}

        # Update properties
        if 'properties' in updates:
            control['properties'].update(updates['properties'])

        if 'position' in updates:
            control['position'] = updates['position']

        if 'size' in updates:
            control['size'] = updates['size']

        return {'success': True, 'control': control}

    # ==================== CODE GENERATION ====================

    async def generate_code(self, form_id: str) -> Dict[str, Any]:
        """
        Generate code for form
        Supports: C# WinForms, VB.NET WinForms, WPF
        """
        if form_id not in self.forms:
            return {'success': False, 'error': 'Form not found'}

        form = self.forms[form_id]

        if form['type'] == 'winforms':
            if form['language'] == 'csharp':
                code = await self._generate_winforms_csharp(form)
            elif form['language'] == 'vbnet':
                code = await self._generate_winforms_vbnet(form)
        elif form['type'] == 'wpf':
            code = await self._generate_wpf_xaml(form)
        else:
            return {'success': False, 'error': 'Unsupported form type'}

        return {
            'success': True,
            'code': code
        }

    async def _generate_winforms_csharp(self, form: Dict[str, Any]) -> Dict[str, str]:
        """Generate C# WinForms code"""
        # Designer code
        designer_code = f"""
namespace {form['name']}App
{{
    partial class {form['name']}
    {{
        private System.ComponentModel.IContainer components = null;

        protected override void Dispose(bool disposing)
        {{
            if (disposing && (components != null))
            {{
                components.Dispose();
            }}
            base.Dispose(disposing);
        }}

        private void InitializeComponent()
        {{
            this.SuspendLayout();

            // Form properties
            this.ClientSize = new System.Drawing.Size({form['size']['width']}, {form['size']['height']});
            this.Name = "{form['name']}";
            this.Text = "{form['title']}";
"""

        # Add controls
        for control in form['controls']:
            control_type = control['type']
            control_name = control['name']
            props = control['properties']
            pos = control['position']
            size = control['size']

            designer_code += f"""
            // {control_name}
            this.{control_name} = new System.Windows.Forms.{control_type}();
            this.{control_name}.Location = new System.Drawing.Point({pos['x']}, {pos['y']});
            this.{control_name}.Name = "{control_name}";
            this.{control_name}.Size = new System.Drawing.Size({size['width']}, {size['height']});
"""

            # Add properties
            for prop_name, prop_value in props.items():
                if prop_name == 'Text':
                    designer_code += f"""            this.{control_name}.Text = "{prop_value}";\n"""

            designer_code += f"""            this.Controls.Add(this.{control_name});\n"""

        designer_code += """
            this.ResumeLayout(false);
        }
"""

        # Add control declarations
        for control in form['controls']:
            designer_code += f"""        private System.Windows.Forms.{control['type']} {control['name']};\n"""

        designer_code += """    }
}
"""

        # Main form code
        main_code = f"""
using System;
using System.Windows.Forms;

namespace {form['name']}App
{{
    public partial class {form['name']} : Form
    {{
        public {form['name']}()
        {{
            InitializeComponent();
        }}
"""

        # Add event handlers
        for control in form['controls']:
            for event_name, event_handler in control['events'].items():
                main_code += f"""
        private void {control['name']}_{event_name}(object sender, EventArgs e)
        {{
            // TODO: Implement event handler
            MessageBox.Show("{control['name']} {event_name} event fired!");
        }}
"""

        main_code += """    }
}
"""

        # Program.cs
        program_code = f"""
using System;
using System.Windows.Forms;

namespace {form['name']}App
{{
    static class Program
    {{
        [STAThread]
        static void Main()
        {{
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new {form['name']}());
        }}
    }}
}}
"""

        return {
            'designer': designer_code,
            'main': main_code,
            'program': program_code
        }

    async def _generate_winforms_vbnet(self, form: Dict[str, Any]) -> Dict[str, str]:
        """Generate VB.NET WinForms code"""
        # Similar to C# but with VB.NET syntax
        designer_code = f"""
<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class {form['name']}
    Inherits System.Windows.Forms.Form

    Private Sub InitializeComponent()
        Me.SuspendLayout()

        ' Form properties
        Me.ClientSize = New System.Drawing.Size({form['size']['width']}, {form['size']['height']})
        Me.Name = "{form['name']}"
        Me.Text = "{form['title']}"
"""

        for control in form['controls']:
            designer_code += f"""
        ' {control['name']}
        Me.{control['name']} = New System.Windows.Forms.{control['type']}()
        Me.{control['name']}.Location = New System.Drawing.Point({control['position']['x']}, {control['position']['y']})
        Me.{control['name']}.Size = New System.Drawing.Size({control['size']['width']}, {control['size']['height']})
        Me.Controls.Add(Me.{control['name']})
"""

        designer_code += """
        Me.ResumeLayout(False)
    End Sub
"""

        # Control declarations
        for control in form['controls']:
            designer_code += f"""    Private WithEvents {control['name']} As System.Windows.Forms.{control['type']}\n"""

        designer_code += "End Class\n"

        main_code = f"""
Public Class {form['name']}
    Public Sub New()
        InitializeComponent()
    End Sub
End Class
"""

        return {
            'designer': designer_code,
            'main': main_code
        }

    async def _generate_wpf_xaml(self, form: Dict[str, Any]) -> Dict[str, str]:
        """Generate WPF XAML code"""
        xaml = f"""
<Window x:Class="{form['name']}App.{form['name']}"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="{form['title']}" Height="{form['size']['height']}" Width="{form['size']['width']}">
    <Grid>
"""

        for control in form['controls']:
            wpf_type = self._map_to_wpf_control(control['type'])
            xaml += f"""        <{wpf_type} x:Name="{control['name']}" """
            xaml += f"""Canvas.Left="{control['position']['x']}" Canvas.Top="{control['position']['y']}" """
            xaml += f"""Width="{control['size']['width']}" Height="{control['size']['height']}" """

            if 'Text' in control['properties']:
                xaml += f"""Content="{control['properties']['Text']}" """

            xaml += "/>\n"

        xaml += """    </Grid>
</Window>
"""

        code_behind = f"""
using System.Windows;

namespace {form['name']}App
{{
    public partial class {form['name']} : Window
    {{
        public {form['name']}()
        {{
            InitializeComponent();
        }}
    }}
}}
"""

        return {
            'xaml': xaml,
            'code_behind': code_behind
        }

    def _map_to_wpf_control(self, winforms_control: str) -> str:
        """Map WinForms control to WPF equivalent"""
        mapping = {
            'Button': 'Button',
            'TextBox': 'TextBox',
            'Label': 'Label',
            'ComboBox': 'ComboBox',
            'ListBox': 'ListBox',
            'CheckBox': 'CheckBox',
            'RadioButton': 'RadioButton',
            'Panel': 'StackPanel',
        }
        return mapping.get(winforms_control, 'Control')

    # ==================== AI IMPROVEMENTS ====================

    async def ai_improve_form(self, form_id: str) -> Dict[str, Any]:
        """
        Use AI to improve form design
        - Suggest better layout
        - Add missing validations
        - Improve UX
        """
        if form_id not in self.forms:
            return {'success': False, 'error': 'Form not found'}

        form = self.forms[form_id]

        suggestions = []

        # Check form size
        if form['size']['width'] < 400 or form['size']['height'] < 300:
            suggestions.append({
                'type': 'layout',
                'message': 'Form size is too small. Consider increasing to at least 800x600'
            })

        # Check for validation on TextBox controls
        text_controls = [c for c in form['controls'] if c['type'] == 'TextBox']
        for control in text_controls:
            if 'Validating' not in control.get('events', {}):
                suggestions.append({
                    'type': 'validation',
                    'control': control['name'],
                    'message': f'Add validation to {control["name"]}'
                })

        # Check for proper button placement
        buttons = [c for c in form['controls'] if c['type'] == 'Button']
        if buttons:
            # Buttons should be at bottom right typically
            for button in buttons:
                if button['position']['y'] < form['size']['height'] - 100:
                    suggestions.append({
                        'type': 'layout',
                        'control': button['name'],
                        'message': f'Consider moving {button["name"]} to bottom of form'
                    })

        return {
            'success': True,
            'suggestions': suggestions
        }

    # ==================== UTILITY ====================

    def _generate_form_id(self) -> str:
        """Generate unique form ID"""
        from datetime import datetime
        return f"form_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    def _generate_control_id(self) -> str:
        """Generate unique control ID"""
        from datetime import datetime
        import random
        return f"ctrl_{datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(1000, 9999)}"

    def get_form(self, form_id: str) -> Optional[Dict[str, Any]]:
        """Get form by ID"""
        return self.forms.get(form_id)

    def list_forms(self) -> List[Dict[str, Any]]:
        """List all forms"""
        return list(self.forms.values())

    def get_available_controls(self) -> Dict[str, Any]:
        """Get list of available controls"""
        return self.components['controls']
