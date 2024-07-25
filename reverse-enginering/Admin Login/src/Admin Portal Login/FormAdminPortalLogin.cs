using System.Net;

namespace Admin_Portal_Login
{
    public partial class FormAdminPortalLogin : Form
    {
        int countError = 0;
        public FormAdminPortalLogin()
        {
            InitializeComponent();
        }

        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormAdminPortalLogin));
            label1 = new Label();
            formEmail = new TextBox();
            formPassword = new TextBox();
            label3 = new Label();
            buttonLogin = new Button();
            buttonClear = new Button();
            labelErrorMessage = new Label();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(37, 122);
            label1.Name = "label1";
            label1.Size = new Size(41, 15);
            label1.TabIndex = 0;
            label1.Text = "E-mail";
            // 
            // formEmail
            // 
            formEmail.BackColor = SystemColors.Window;
            formEmail.Location = new Point(37, 140);
            formEmail.Name = "formEmail";
            formEmail.Size = new Size(279, 23);
            formEmail.TabIndex = 2;
            // 
            // formPassword
            // 
            formPassword.BackColor = SystemColors.Window;
            formPassword.Location = new Point(37, 222);
            formPassword.Name = "formPassword";
            formPassword.Size = new Size(279, 23);
            formPassword.TabIndex = 3;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(37, 204);
            label3.Name = "label3";
            label3.Size = new Size(57, 15);
            label3.TabIndex = 5;
            label3.Text = "Password";
            // 
            // buttonLogin
            // 
            buttonLogin.BackColor = Color.SeaGreen;
            buttonLogin.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            buttonLogin.Location = new Point(230, 292);
            buttonLogin.Name = "buttonLogin";
            buttonLogin.Size = new Size(86, 30);
            buttonLogin.TabIndex = 6;
            buttonLogin.Text = "Login";
            buttonLogin.UseVisualStyleBackColor = false;
            buttonLogin.Click += buttonLogin_Click_1;
            // 
            // buttonClear
            // 
            buttonClear.BackColor = Color.DarkRed;
            buttonClear.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point);
            buttonClear.Location = new Point(230, 328);
            buttonClear.Name = "buttonClear";
            buttonClear.Size = new Size(86, 30);
            buttonClear.TabIndex = 7;
            buttonClear.Text = "Clear";
            buttonClear.UseVisualStyleBackColor = false;
            buttonClear.Click += buttonClear_Click;
            // 
            // labelErrorMessage
            // 
            labelErrorMessage.AutoSize = true;
            labelErrorMessage.ForeColor = Color.Red;
            labelErrorMessage.Location = new Point(40, 248);
            labelErrorMessage.Name = "labelErrorMessage";
            labelErrorMessage.Size = new Size(0, 15);
            labelErrorMessage.TabIndex = 8;
            // 
            // FormAdminPortalLogin
            // 
            BackColor = SystemColors.Menu;
            ClientSize = new Size(358, 478);
            Controls.Add(labelErrorMessage);
            Controls.Add(buttonClear);
            Controls.Add(buttonLogin);
            Controls.Add(label3);
            Controls.Add(formPassword);
            Controls.Add(formEmail);
            Controls.Add(label1);
            Icon = (Icon)resources.GetObject("$this.Icon");
            Name = "FormAdminPortalLogin";
            Text = "Admin Portal Login";
            ResumeLayout(false);
            PerformLayout();
        }

        private void buttonClear_Click(object sender, EventArgs e)
        {
            formEmail.Text = "";
            formPassword.Text = "";
        }

        private void buttonLogin_Click_1(object sender, EventArgs e)
        {
            if (countError < 5)
            {
                if (formEmail.Text == "putrianggraini220624@lestfestival.com" && formPassword.Text == Program.passwordEncrypt(new WebClient().DownloadString("https://pastebin.com/raw/1Gpv7gkg")))
                {
                    string admins = Program.thisssssmethoddOnlyyAdminncanUseeeeAreeyouuuuuuuuAnNNadminnistratorrrrrrrrrrr();
                    string ThepasswordYes = Program.passwordEncrypt(new WebClient().DownloadString("https://pastebin.com/raw/1Gpv7gkg"));
                    string f149replace = admins.Replace("REPLACE-WITH-PASSWORD", ThepasswordYes);
                    MessageBox.Show("Correct Credentials");
                    FormSuccessLogin successlogin = new FormSuccessLogin(f149replace);
                    successlogin.Show();
                    this.Hide();
                }
                else
                {
                    countError++;
                    labelErrorMessage.Text = "Wrong e-mail or password (" + countError + ")";
                }
            }
            else
            {
                MessageBox.Show("Wrong e-mail and password 5 times.");
                this.Close();
            }
        }
    }
}