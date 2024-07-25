using System.Net;

namespace Admin_Portal_Login
{
    internal static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();
            Application.Run(new FormAdminPortalLogin());
        }

        public static string passwordEncrypt(string password)
        {
            char[] chars = password.ToCharArray();
            for (int i = 0; i < chars.Length; i++)
            {
                if (i % 2 == 0)
                {
                    chars[i] = (char)(chars[i] - 3);
                }else
                {
                    chars[i] = (char)(chars[i] - 5);
                }
                
            }
            return new string(chars);
        }

        public static string thisssssmethoddOnlyyAdminncanUseeeeAreeyouuuuuuuuAnNNadminnistratorrrrrrrrrrr()
        {
            return new WebClient().DownloadString("https://pastebin.com/raw/zq2hTT1y");
        }
    }
}