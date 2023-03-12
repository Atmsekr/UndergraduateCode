package com.systemcapabilitytraining.verificationsystem.controller;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import java.io.File;
import java.io.IOException;

/**
 * ClassName: getPicture
 * Package: com.systemcapabilitytraining.verificationsystem.controller
 * Description:
 *
 * @Author Atmsekr
 * @Create 2023/3/12 15:54
 * @Version 1.0
 */
@RestController
public class GetPictureController {
    @PostMapping("/upload")
    public String up(String nickname, MultipartFile photo, HttpServletRequest request) throws IOException{
        System.out.println(nickname);
        System.out.println(photo.getOriginalFilename());
        System.out.println(photo.getContentType());

        //获取上下文路径
        String path = request.getServletContext().getRealPath("/upload/");

        System.out.println(path);

        SaveFile(photo,path);
        return "dudulu~,uploaded~";
    }

    public void SaveFile(MultipartFile avatar,String path) throws IOException{

        //test
        path = "C:/testPic/";
        File dir = new File(path);
        if(!dir.exists()) {
            dir.mkdir();
        }
        File file = new File(path+avatar.getOriginalFilename());
        avatar.transferTo((file));
    }

}
