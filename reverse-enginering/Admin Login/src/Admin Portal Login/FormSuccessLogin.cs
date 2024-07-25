using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Admin_Portal_Login
{
    public partial class FormSuccessLogin : Form
    {
        public FormSuccessLogin(string flagtoBox)
        {
            InitializeComponent();
            this.textBoxFlag.Text = flagtoBox;
        }

    }
}
