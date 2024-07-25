namespace Admin_Portal_Login
{
    partial class FormSuccessLogin
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormSuccessLogin));
            textBoxFlag = new TextBox();
            labelCongratulation = new Label();
            pictureBox1 = new PictureBox();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            SuspendLayout();
            // 
            // textBoxFlag
            // 
            textBoxFlag.Location = new Point(37, 140);
            textBoxFlag.Name = "textBoxFlag";
            textBoxFlag.ReadOnly = true;
            textBoxFlag.Size = new Size(279, 23);
            textBoxFlag.TabIndex = 0;
            // 
            // labelCongratulation
            // 
            labelCongratulation.AutoSize = true;
            labelCongratulation.Location = new Point(84, 122);
            labelCongratulation.Name = "labelCongratulation";
            labelCongratulation.Size = new Size(179, 15);
            labelCongratulation.TabIndex = 1;
            labelCongratulation.Text = "Congratulations, here's your flag";
            // 
            // pictureBox1
            // 
            pictureBox1.Image = (Image)resources.GetObject("pictureBox1.Image");
            pictureBox1.Location = new Point(37, 217);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(279, 224);
            pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
            pictureBox1.TabIndex = 2;
            pictureBox1.TabStop = false;
            // 
            // FormSuccessLogin
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Menu;
            ClientSize = new Size(358, 478);
            Controls.Add(pictureBox1);
            Controls.Add(labelCongratulation);
            Controls.Add(textBoxFlag);
            Icon = (Icon)resources.GetObject("$this.Icon");
            Name = "FormSuccessLogin";
            Text = "Welcome back, Anisa";
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox textBoxFlag;
        private Label labelCongratulation;
        private PictureBox pictureBox1;
    }
}