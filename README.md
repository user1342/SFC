<p align="center">
    <img width=100% src="sfc.gif">
  </a>
</p>
<p align="center"> 📁 Simple Folder Comparison ⚙️ </b> </p>

<div align="center">

![GitHub contributors](https://img.shields.io/github/contributors/user1342/SFC)
![GitHub Repo stars](https://img.shields.io/github/stars/user1342/SFC?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/user1342/SFC?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/user1342/SFC)
<br>
</div>

# Simple Folder Compare Tool

The Simple Folder Compare Tool is a command-line utility designed to compare the contents of two folders, identifying modifications, additions, and removals. It generates a detailed report listing the changes along with their paths.

## ⚙️ Usage

### Requirements

The tool requires Python 3.x to be installed. Install the required dependencies using the following command:

```
pip install -r requirements.txt
```

### Running the Tool

To compare two folders and generate a report, use the following command:

```bash
python compare.py source_folder target_folder -o output_report.txt
```

Replace source_folder and target_folder with the paths to the folders you want to compare. The -o option specifies the output file for the report.

📜 Output
The tool generates a plain text file (output_report.txt by default) listing modifications, additions, and removals along with their paths in a structured manner. For example:

```
Modified: Documentation\ABI\testing\sysfs-bus-iio
Modified: Documentation\ABI\testing\sysfs-devices-system-cpu
Modified: Documentation\DocBook\libata.tmpl
Modified: Documentation\devicetree\bindings\net\nfc\nxp-nci.txt
Modified: Documentation\devicetree\bindings\net\nfc\pn544.txt
Modified: Documentation\devicetree\bindings\sound\wm8994.txt
Modified: Documentation\filesystems\affs.txt
Added: Documentation\hw-vuln\special-register-buffer-data-sampling.rst
Modified: Documentation\networking\ip-sysctl.txt
Modified: Documentation\networking\l2tp.txt
Modified: Documentation\kernel-parameters.txt
Modified: arch\alpha\include\asm\io.h
Modified: arch\arc\include\asm\elf.h
Modified: arch\arm\mach-tegra\tegra.c
Modified: arch\arm\mm\cache-l2x0.c
Modified: arch\arm\mm\proc-macros.S
Modified: arch\arm\plat-samsung\Kconfig
Modified: arch\arm\Kconfig
Modified: arch\arm64\boot\dts\xilinx\zynqmp.dtsi
Removed: arch\arm64\configs\taimen_defconfig
```

🙏 Contributions
Contributions to the Simple Folder Compare Tool are welcome. If you would like to contribute, please follow the guidelines provided in the CONTRIBUTING.md file.
- Fork the repository to your own GitHub account.
- Create a new branch with a descriptive name for your contribution.
- Make your changes and test them thoroughly.
- Submit a pull request to the main repository, including a detailed description of your changes and any relevant
  documentation.
- Wait for feedback from the maintainers and address any comments or suggestions (if any).
- Once your changes have been reviewed and approved, they will be merged into the main repository.


🐛 Bug Reports and Feature Requests
If you encounter any bugs or have suggestions for new features, please open an issue in the GitHub repository.

📄 License
[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)
