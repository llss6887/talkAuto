package com.heimamba.utils;


import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.protocol.HTTP;
import org.springframework.beans.factory.annotation.Autowired;

public class GitalkAuto {

    public static Object autoTalk(String username,String repo, String uri, String blogUrl,String title, String token) throws Exception{
        String url = "https://api.github.com/repos/"+username+"/"+repo+"/issues";
        String param = String.format("{\"title\":\"%s\",\"labels\":[\"%s\", \"Gitalk\"],\"body\":\"%s%s\\n\\n\"}"
                                            , title, uri, blogUrl, uri);
        HttpClient client = HttpClients.createDefault();
        HttpPost post = new HttpPost(url);
        StringEntity entity = new StringEntity(param, HTTP.UTF_8);
        post.setHeader("accept", "*/*");
        post.setHeader("connection", "Keep-Alive");
        post.setHeader("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36");
        post.setHeader("Authorization", "token "+token);
        post.setEntity(entity);
        HttpResponse response = client.execute(post);
        return response.getEntity();
    }
}
